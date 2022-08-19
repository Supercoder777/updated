import { chromium } from "playwright";



describe("testing with playwright", () =>{
    test("login into hub", async () => {
        const browser = await chromium.launch({
          headless: false
        });
        const context = await browser.newContext();
        // Open new page
        const page = await context.newPage();
        // Go to https://hub.knime.com/
        await page.goto('https://hub.knime.com/');
        // Click text=Accept and close
        await page.locator('text=Accept and close').click();
        // Click text=Sign in
        await page.locator('text=Sign in').click();
        await page.waitForURL('https://www.knime.com/user/login?destination=/oauth2/authorize');
        // Fill [placeholder="Username or email address"]
        await page.locator('[placeholder="Username or email address"]').fill('samuel4luve@yahoo.com');
        // Press Tab
        await page.locator('[placeholder="Username or email address"]').press('Tab');
        // Fill [placeholder="Password"]
        await page.locator('[placeholder="Password"]').fill('zAddi623_');
        // Click button:has-text("Sign in")
        await page.locator('button:has-text("Sign in")').click();
        await page.waitForURL('https://hub.knime.com/');
        // Click button:has-text("D")
        await page.locator('button:has-text("D")').click();
        // Click text=Logout
        await page.locator('text=Logout').click();
        await page.waitForURL('https://hub.knime.com/');
        // ---------------------
        await context.close();
        await browser.close(); 
    })


    test("spaces", async () => {
        const browser = await chromium.launch({
          headless: false
        });
        const context = await browser.newContext();
        // Open new page
        const page = await context.newPage();
        // Go to https://hub.knime.com/
        await page.goto('https://hub.knime.com/');
        // Click text=Accept and close
        await page.locator('text=Accept and close').click();
        // Click text=Sign in
        await page.locator('text=Sign in').click();
        await page.waitForURL('https://www.knime.com/user/login?destination=/oauth2/authorize');
        // Fill [placeholder="Username or email address"]
        await page.locator('[placeholder="Username or email address"]').fill('samuel4luve@yahoo.com');
        // Press Tab
        await page.locator('[placeholder="Username or email address"]').press('Tab');
        // Fill [placeholder="Password"]
        await page.locator('[placeholder="Password"]').fill('zAddi623_');
        // Click button:has-text("Sign in")
        await page.locator('button:has-text("Sign in")').click();
        await page.waitForURL('https://hub.knime.com/');
        // Click button:has-text("D")
        await page.locator('button:has-text("D")').click();
        // Click span:has-text("Spaces")
        await page.locator('span:has-text("Spaces")').click();
        await page.waitForURL('https://hub.knime.com/damilola001/spaces');
         // Click button:has-text("Public space")
         await page.locator('button:has-text("Public space")').click();
        await page.waitForURL('https://hub.knime.com/damilola001/spaces/New%20space%2028/latest/~kigWTo87-mfEhBlE/');
         // Click text=Public spacePublic space Manage contributors D >> button >> nth=0
        await page.locator('text=Public spacePublic space Manage contributors D >> button').first().click();
        // Click text=0 Like Copy short link More >> button >> nth=2
        await page.locator('text=0 Like Copy short link More >> button').nth(2).click();
        // Click text=Delete space
        await page.locator('text=Delete space').click();
        // Click [placeholder="space name"]
        await page.locator('[placeholder="space name"]').click();
         // Fill [placeholder="space name"]
        await page.locator('[placeholder="space name"]').fill('New space 28');
        // Click text=I understand the consequences, delete space permanently
        await page.locator('text=I understand the consequences, delete space permanently').click();
        await page.waitForURL('https://hub.knime.com/damilola001/spaces');
         // Click nav[role="navigation"] button:has-text("D")
        await page.locator('nav[role="navigation"] button:has-text("D")').click();
        // Click text=Logout
        await page.locator('text=Logout').click();
        await page.waitForURL('https://hub.knime.com/');
         // ---------------------
         await context.close();
         await browser.close();

    })
    

})