import asyncio
from typing import Optional
from playwright.async_api import async_playwright, Browser, Page, Playwright

from app.utils.helpers import hash_content, logger

from app.config import settings


class BrowserClient:
    """
    Browser automation tool using Playwright.

    Handles JavaScript-rendered pages, dynamic content, and screenshot capture
    for vision analysis.
    """

    def __init__(self):
        self.playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None
        self._initialized = False

    async def initialize(self):
        if self._initialized:
            return

        try:
            self.playwright = await async_playwright().start()

            # Launch browser
            self.browser = await self.playwright.chromium.launch(
                headless=True,
                args=["--disable-blink-features=AutomationControlled"], # Avoid detection
            )

            self._initialized = True
            
        except Exception as e:
            logger.error(f"Failed to initialize browser: {e}")
            raise

    async def close(self) -> None:
        """Cleanup browser resources."""
        if self.browser:
            logger.info("Closing browser")
            await self.browser.close()
            self.browser = None

        if self.playwright:
            await self.playwright.stop()
            self.playwright = None

        self._initialized = False

    async def __aenter__(self):
        """Async context manager entry."""
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
