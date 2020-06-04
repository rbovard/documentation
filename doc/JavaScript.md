# JavaScript

* [Auto refresh image](#auto-refresh-image)

## Auto refresh image

```
window.onload = function() {
    var image = document.getElementById("img");

    function updateImage() {
        image.src = image.src.split("?")[0] + "?" + new Date().getTime();
    }

    setInterval(updateImage, 1000);
}
```

```
<img src="<image.jpg>" id="img" />
```
