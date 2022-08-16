import { chromium } from "playwright";
import { test, expect } from '@playwright/test';



describe("learning playwright", () => {
    
    test("knime work", async ({ }) => {
       
});

    })

xtest("login", async() => {

  const browser = await chromium.launch({
    headless: false
  });  
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto("https://hub.knime.com");
  // await page.close()
  // await context.close()
  // await browser.close()



 
})
