# WaifuLabs

A unofficial wrapper for WaifuLabs

## Generate a waifu
```python
import waifulabs

waifu = waifulabs.GenerateWaifu()
```

## Generate 16 waifus
```python
import waifulabs

waifu = waifulabs.GenerateWaifus()
```

## Save a waifu
```python
import waifulabs

waifu = waifulabs.GenerateWaifu()

waifu.save("waifus/mywaifu.png")
```

## Generate a big waifu (Higher quality)
```python
import waifulabs

waifu = waifulabs.GenerateWaifu()
bigwaifu = waifu.GenerateBigWaifu()

bigwaifu.save("waifus/mybigwaifu.png")
```

## Generate a waifu product
```python
import waifulabs

waifu = waifulabs.GenerateWaifu()
waifupillow = waifu.GenerateProduct(waifulabs.PILLOW)
waifuposter = waifu.GenerateProduct(waifulabs.POSTER)

waifupillow.save("waifus/mywaifupillow.png")
waifuposter.save("waifus/mywaifuposter.png")
```

# About steps

Steps are the steps that waifulabs uses to modify a waifu.

Step 0:
> Choose a template waifu

Step 1:
> Change the color palette

Step 2:
> File tuning of details

Step 3:
> Pose

Steps are available for `GenerateWaifu` and `GenerateWaifus`

# Build from source
On Windows you can run `install.bat` in cmd

On Linux and Mac you can run `install.sh` in a terminal