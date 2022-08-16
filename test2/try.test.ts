import { chromium } from "playwright";

describe(" playing Wright", () => {

    test("trick", async () => {

        const browser = await chromium.launch({
            // headless: false
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
          // Click [placeholder="Username or email address"]
          await page.locator('[placeholder="Username or email address"]').click();
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
          // Click button:has-text("Private space")
          await page.locator('button:has-text("Private space")').click();
          await page.waitForURL('https://hub.knime.com/damilola001/spaces/New%20space%202/latest/~d_dgGdFQ5omKQI6V/');
          // Fill textarea
          await page.locator('textarea').fill('testP01');
          // Press a with modifiers
          await page.locator('textarea').press('Meta+a');
          // Click text=Private spacePrivate space D >> button >> nth=0
          await page.locator('text=Private spacePrivate space D >> button').first().click();
          await page.waitForURL('https://hub.knime.com/damilola001/spaces/testP01/latest/~d_dgGdFQ5omKQI6V/');
          // Click text=0 Like Copy short link More >> button >> nth=2
          await page.locator('text=0 Like Copy short link More >> button').nth(2).click();
          // Click text=Delete space
          await page.locator('text=Delete space').click();
          // Click [placeholder="space name"]
          await page.locator('[placeholder="space name"]').click();
          // Fill [placeholder="space name"]
          await page.locator('[placeholder="space name"]').fill('// Click text=Accept and close   await page.locator(\'text=Accept and close\').click();   // Click text=Sign in   await page.locator(\'text=Sign in\').click();   await expect(page).toHaveURL(\'https://www.knime.com/user/login?destination=/oauth2/authorize\');   // Click [placeholder="Username or email address"]   await page.locator(\'[placeholder="Username or email address"]\').click();   // Fill [placeholder="Username or email address"]   await page.locator(\'[placeholder="Username or email address"]\').fill(\'samuel4luve@yahoo.com\');   // Click [placeholder="Password"]   await page.locator(\'[placeholder="Password"]\').click();   // Fill [placeholder="Password"]   await page.locator(\'[placeholder="Password"]\').fill(\'zAddi623_\');   // Click button:has-text("Sign in")   await page.locator(\'button:has-text("Sign in")\').click();   await expect(page).toHaveURL(\'https://hub.knime.com/\');   // Click button:has-text("D")   await page.locator(\'button:has-text("D")\').click();   // Click span:has-text("Spaces")   await page.locator(\'span:has-text("Spaces")\').click();   await expect(page).toHaveURL(\'https://hub.knime.com/damilola001/spaces\');   // Click button:has-text("Public space")   await page.locator(\'button:has-text("Public space")\').click();   // Click text=Private space Public space   await page.locator(\'text=Private space Public space\').click();   await expect(page).toHaveURL(\'https://hub.knime.com/damilola001/spaces/New%20space%202/latest/~_-agiBeLc-XmKxNH/\');   // Triple click textarea   await page.locator(\'textarea\').click({     clickCount: 3   });   // Fill textarea   await page.locator(\'textarea\').fill(\'new space developed\');   // Click text=Public spacePublic space Manage contributors D >> button >> nth=0   await page.locator(\'text=Public spacePublic space Manage contributors D >> button\').first().click();   // Click text=Public spacePublic space Manage contributors D >> button >> nth=0   await page.locator(\'text=Public spacePublic space Manage contributors D >> button\').first().click();   await expect(page).toHaveURL(\'https://hub.knime.com/damilola001/spaces/new%20space%20developed/latest/~_-agiBeLc-XmKxNH/\');   // Click button:has-text("0")   await page.locator(\'button:has-text("0")\').click();   // Click text=1 Like Copy short link More >> button >> nth=2   await page.locator(\'text=1 Like Copy short link More >> button\').nth(2).click();   // Click text=Delete space   await page.locator(\'text=Delete space\').click();   // Click [placeholder="space name"]   await page.locator(\'[placeholder="space name"]\').click();   // Fill [placeholder="space name"]   await page.locator(\'[placeholder="space name"]\').fill(\'new space developed\');   // Click text=I understand the consequences, delete space permanently   await page.locator(\'text=I understand the consequences, delete space permanently\').click();   await expect(page).toHaveURL(\'https://hub.knime.com/damilola001/spaces\');   // Click nav[role="navigation"] button:has-text("D")   await page.locator(\'nav[role="navigation"] button:has-text("D")\').click();   // Click text=Logout   await page.locator(\'text=Logout\').click();   await expect(page).toHaveURL(\'https://hub.knime.com/\'); });');
          // Press z with modifiers
          await page.locator('[placeholder="space name"]').press('Meta+z');
          // Fill [placeholder="space name"]
          await page.locator('[placeholder="space name"]').fill('testP01');
          // Click text=I understand the consequences, delete space permanently
          await page.locator('text=I understand the consequences, delete space permanently').click();
          await page.waitForURL('https://hub.knime.com/damilola001/spaces');
          // ---------------------
          await context.close();
          await browser.close();
        })
    })