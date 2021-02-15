# WaifuLabs

A unofficial wrapper for WaifuLabs (WaifuLabs用の非公式Pythonパッケージ)

![PyPI](https://img.shields.io/pypi/v/waifulabs)
![PyPI - Downloads](https://img.shields.io/pypi/dm/waifulabs)
![GitHub issues](https://img.shields.io/github/issues/Taromaruu/WaifuLabs)
![GitHub](https://img.shields.io/github/license/Taromaruu/WaifuLabs)

## Generate a waifu (一つつのWaifuを生成します)
```python
import waifulabs

waifu = waifulabs.GenerateWaifu()
```

## Generate 16 waifus (16のWaifuを生成する)
```python
import waifulabs

waifu = waifulabs.GenerateWaifus()
```

## Save a waifu (Waifuをコンピューターに保存します)
```python
import waifulabs

waifu = waifulabs.GenerateWaifu()

waifu.save("waifus/mywaifu.png")
```

## Generate a big waifu (Higher quality) (大きなWaifuを生成する)
```python
import waifulabs

waifu = waifulabs.GenerateWaifu()
bigwaifu = waifu.GenerateBigWaifu()

bigwaifu.save("waifus/mybigwaifu.png")
```

## Generate a waifu product (Waifu製品を生成する)
```python
import waifulabs

waifu = waifulabs.GenerateWaifu()
waifupillow = waifu.GenerateProduct(waifulabs.PILLOW)
waifuposter = waifu.GenerateProduct(waifulabs.POSTER)

waifupillow.save("waifus/mywaifupillow.png")
waifuposter.save("waifus/mywaifuposter.png")
```

# About steps (ステップについて)

Steps is the seed waifulabs uses to modify a waifu. (ステップはWaifuの外観を変更します)

Step 0: (ステップ0)
> Choose a template waifu (テンプレートWaifuを選択してください)

Step 1: (ステップ1)
> Change the color palette (カラーパレットを変更する)

Step 2: (ステップ2)
> File tuning of details (詳細を微調整)

Step 3: (ステップ3)
> Change Pose (ポーズを変える)

Steps are available for `GenerateWaifu` and `GenerateWaifus` (Stepは、 `GenerateWaifu`と` GenerateWaifus`で機能します)

# Build from source (コードから構築)
On Windows run `install.bat` in cmd (Windowsでは、cmdで `install.bat`を実行します)

On Linux and Mac you can run `install.sh` in a terminal (MacまたはLinuxでは、ターミナルで `install.sh`を実行します)
