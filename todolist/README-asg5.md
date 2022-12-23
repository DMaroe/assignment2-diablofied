Name : Dylan Dahran Pribadi
NPM  : 2106720872

1. What is the difference between Inline, Internal, and External CSS? What are the advantages and disadvantages of each style?

Inline CSS refers to styling an HTML element using the "style" attribute within the element's tag. For example:

```html
    <p style="color: blue; font-size: 14px">This is a paragraph</p>
```

Internal CSS refers to styling an HTML element using a "style" tag within the head of the HTML document. The style rules apply to the entire document, so you don't need to specify the element for each rule. For example:

```html
<head>
  <style>
    p {
      color: blue;
      font-size: 14px;
    }
  </style>
</head>

```
External CSS refers to styling an HTML element using a separate CSS file that is linked to the HTML document. The CSS rules apply to the entire document, so you don't need to specify the element for each rule. To link the CSS file, you would use the "link" tag within the head of the HTML document:

```html
<head>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>

```

The advantage of inline CSS is that it allows you to apply styles directly to a specific element, which can be useful if you only want to style one or a few elements on a page. The disadvantage is that it can be difficult to maintain and can make the HTML code harder to read.

The advantage of internal CSS is that it allows you to style the elements of a single HTML document, which can be useful if you only have a few pages on your website. The disadvantage is that you have to repeat the same styles for each page, which can be time-consuming and makes it difficult to make global changes to your website.

The advantage of external CSS is that it allows you to style multiple HTML documents at once, which makes it easier to make global changes to your website. It also keeps your HTML code cleaner and easier to read, since the styles are in a separate file. The disadvantage is that it requires an extra step to link the CSS file to each HTML document, and it may take longer to load the page if the CSS file is large.

In general, it is best practice to use external CSS for styling a website, since it allows for the most flexibility and maintainability. However, each method has its own use case and it's up to the developer to decide which method is best for a particular situation.

2. Describe the HTML5 tags that you know.

<footer>: Represents the footer of a section or page.
<header>: Represents the header of a section or page.
<main>: Represents the main content of a page.
<mark>: Represents text that should be highlighted or marked as important.
<nav>: Represents a section of the page that contains navigation links.
<output>: Represents the result of a calculation or user action.
<picture>: Allows developers to specify different images to display at different screen sizes or resolutions.

3. Describe the types of CSS selectors you know.

Type selectors: Select elements based on their element type (e.g., p selects all <p> elements).

Class selectors: Select elements based on their class attribute (e.g., .warning selects all elements with a class of "warning").

ID selectors: Select elements based on their id attribute (e.g., #main selects the element with an id of "main").

Attribute selectors: Select elements based on the presence or value of an attribute (e.g., [type="text"] selects all elements with a type attribute set to "text").

Pseudo-class selectors: Select elements based on their state or position (e.g., :hover selects elements that are being hovered over by the mouse).

Pseudo-element selectors: Select specific parts of an element (e.g., ::before selects the content before an element).

4. Explain how you would implement the checklist above.