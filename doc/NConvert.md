NConvert
========

* [Reduce JPEG images](#reduce-jpeg-images)

Reduce JPEG images
------------------

```batchfile
for /f %%f in ('dir /s/b <path>\*.jpg') do nconvert -out jpeg -resize <min-width> <min-height> -ratio -rtype lanczos -rflag decr -overwrite %%f
```
