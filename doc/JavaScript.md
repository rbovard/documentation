# JavaScript

* [Auto refresh image](#auto-refresh-image)
* [Detect mobile browser](#detect-mobile-browser)

## Auto refresh image

```js
window.onload = function() {
    const image = document.getElementById("img");

    function updateImage() {
        image.src = image.src.split("?")[0] + "?" + new Date().getTime();
    }

    setInterval(updateImage, 1000);
}
```

```html
<img src="<image.jpg>" id="img" />
```

## Detect mobile browser

```js
const isMobileDevice = /Mobi/i.test(window.navigator.userAgent);
```
