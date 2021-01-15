import waifulabs

w = waifulabs.GenerateWaifu()
w.save("base.png")

for i in range(5):
    x = waifulabs.GenerateWaifu(w.seeds, 1)
    x.save(f"{i}.png")