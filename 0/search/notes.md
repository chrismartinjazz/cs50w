# Search

## Google Search Queries

### Standard

https://www.google.com/search
?q=anything
&sca_esv=eb0e27f25aa9f8c7
&sxsrf=AKL5yDg3dYxeir29tfteG9kxi4JdDpUAsA%3A1795197117158
&source=hp
&ei=vYgAa6SuB4rH0-kPn4CV8AY
&iflsig=AHSINFcAAAAAawCWzc4JZqGTXKPR8uSB8Jad5pRbe6ml
&ved=2ahUKEwjkgN-zjpeYAxWK4zQHHR9ABW4Q4dUDegQIABAq
&uact=5
&oq=anything
&gs_lp=Egdnd3Mtd2l6Ighhbnl0aGluZzINEAAYgAQYigUYQxixAzIQEC4YgAQYigUYQxixAxiDATIQEAAYgAQYigUYQxixAxiDATILEAAYgAQYsQMYgwEyBBAAGAMyCBAAGIAEGLQHMggQABiABBi0BzIIEC4YgAQYsQMyCxAAGIAEGLEDGIMBMg4QABiABBiKBRixAxiDAUi4C1CeBVjdCnABeACQAQCYAakBoAGlCKoBAzAuN7gBA8gBAPgBAZgCCKAC4gioAgrCAgcQIxjqAhgnwgIQECMYnQYY6AYY3QUY6gIYJ8ICBxAuGOoCGCfCAgQQIxgnwgILEAAYgAQYigUYkQLCAgoQABiABBiKBRhDwgIREAAYgAQYigUYkQIYsQMYgwHCAhYQLhiABBiKBRhDGLEDGIMBGMcBGNEDwgIREC4YgAQYsQMYyQMYxwEY0QPCAgUQABiABMICCxAAGIAEGIoFGJIDwgIWEC4YgAQYigUYQxixAxjJAxjHARjRA8ICCBAAGIAEGJIDwgIIEAAYgAQYsQOYAx_xBe3tBhzP3blakgcDMS43oAfTPrIHAzAuN7gHwwjCBwkwLjIuNS4wLjHIBymACAE
&sclient=gws-wiz

https://www.google.come/search?q=anything

### Image

https://www.google.com/search
?q=anything
&sca_esv=eb0e27f25aa9f8c7
&udm=2
&biw=1278
&bih=1278
&sxsrf=AKL5yDjJbFTc7HesOmC-BCuEDh3UZy9Snw%3A1795197661164
&ei=3YoAa9LLCZ3k2roPubfE0AY
&ved=2ahUKEwiSrpS3kJeYAxUdslYBHbkbEWoQ4dUDegQIBhAN
&uact=5
&oq=anything
&gs_lp=Egtnd3Mtd2l6LWltZyIIYW55dGhpbmcyEBAAGIAEGIoFGEMYsQMYgwEyCxAAGIAEGLEDGIMBMgQQABgDMgUQABiABDIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBMg4QABiABBiKBRixAxiDATIOEAAYgAQYigUYsQMYgwEyBRAAGIAEMggQABiABBixA0jUJ1CuIFjZJnACeACQAQCYAZYBoAH6B6oBAzAuN7gBA8gBAPgBAZgCCaACowjCAg0QABiABBiKBRhDGLEDwgIGEAAYBxgewgIKEAAYgAQYigUYQ8ICBxAjGMkCGCeYAwCIBgGSBwMyLjegB_ghsgcDMC43uAeXCMIHBTAuMi43yAccgAgB
&sclient=gws-wiz-img

https://www.google.com/search?q=anything&udm=2

### Advanced

https://www.google.com/search
?as_st=y
&as_q=anything+everything
&as_epq=anything+and+everything
&as_eq=something
&as_sitesearch=&imgar=&cr=&as_filetype=&tbs=&authuser=0

https://www.google.com/search?as_q=anything+everything&as_epq=implies+a+choice+from+an+unlimited+range+of+possibilities&as_eq=nonsense+bravado

Parameters:

- as_q (all these words)
- as_epq (this exact word or phrase)
- as_eq (none of these words)
- as_oq (any of these words)

https://www.google.com/search?as_q=magnolias|intercontinental|rabbi

## Specification

Pages. Your website should have at least three pages: one for regular Google Search (which must be called index.html), one for Google Image Search, and one for Google Advanced Search.

    On the Google Search page, there should be links in the upper-right of the page to go to Image Search or Advanced Search. On each of the other two pages, there should be a link in the upper-right to go back to Google Search.

Text Search. On the Google Search page, the user should be able to type in a query, click “Google Search”, and be taken to the Google search results for that page.

    Like Google’s own, your search bar should be centered with rounded corners. The search button should also be centered, and should be beneath the search bar.

Image Search. On the Google Image Search page, the user should be able to type in a query, click a search button, and be taken to the Google Image search results for that page.
Advanced Search. On the Google Advanced Search page, the user should be able to provide input for the following four fields (the below was taken from Google’s own advanced search options as they looked prior to a change in 2026, and you should use the following search fields only)

    Find pages with… “all these words:”
    Find pages with… “this exact word or phrase:”
    Find pages with… “any of these words:”
    Find pages with… “none of these words:”

Visual Consistency. Like Google’s own Advanced Search page, the four options should be stacked vertically, and all of the text fields should be left aligned.

    Consistent with Google’s own CSS, the “Advanced Search” button should be blue with white text.
    When the “Advanced Search” button is clicked, the user should be taken to the search results page for their given query.

Lucky. Add an “I’m Feeling Lucky” button to the main Google Search page. Consistent with Google’s own behavior, clicking this link should take users directly to the first Google search result for the query, bypassing the normal results page.

    You may encounter a redirect notice when using the “I’m Feeling Lucky” button. Not to worry! This is an expected consequence of a security feature implemented by Google.

Aesthetics. The CSS you write should resemble Google’s own aesthetics.

## Hints

    To determine what the parameter names should be, you’re welcome to experiment with making Google searches, and looking at the resulting URL. It may also be helpful to open the “Network” inspector (accessible in Google Chrome by choosing View -> Developer -> Developer Tools) to view details about requests your browser makes to Google.
        Any <input> element (whether its type is text, submit, number, or something else entirely) can have name and value attributes that will become GET parameters when a form is submitted.
        You may also find it helpful to look at Google’s own HTML to answer these questions. In most browsers, you can control-click or right-click on a page and choose “View Page Source” to view the page’s underlying HTML.
    To include an input field in a form that users cannot see or modify, you can use a “hidden” input field.
