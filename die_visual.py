from die import Die
import pygal

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
freqencies = []
for value in range(1, die.num_sides + 1):
    freqency = results.count(value)
    freqencies.append(freqency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequencr of Result"

hist.add('D6', freqencies)
hist.render_to_file('die_visual.svg')