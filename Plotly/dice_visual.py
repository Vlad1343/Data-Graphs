

# from plotly.graph_objs import Bar, Layout
# from plotly import offline

# from die import Die


# # Create two D6
# die_1 = Die()
# die_2 = Die()

# # Roll the die a few times and store the results
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# # Analyze the results
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # Visualize the results
# x_values = list(range(2, max_result + 1))
# data = [Bar(x=x_values, y=frequencies)]

# x_axis_config = {'title': 'Result', 'dtick': 1} # 'dtick': 1 ensures every tick is shown
# y_axis_config = {'title': 'Frequency of Result'}
# my_layout = Layout(title='Results of Rolling two D6 dies 1000 Times',
#                    xaxis=x_axis_config, yaxis=y_axis_config)
# offline.plot({'data': data, 'layout': my_layout}, filename='cube/d6_d6.html')













from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# Create D6 and D10
die_1 = Die()
die_2 = Die(10)

# Roll the die a few times and store the results
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1} # 'dtick': 1 ensures every tick is shown
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of Rolling two a D6 and a D10 50000 Times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='cube/d6_d10.html')


