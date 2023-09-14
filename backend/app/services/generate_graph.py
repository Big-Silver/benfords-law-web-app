import os
import matplotlib.pyplot as plt

def generate_bar_chart(data, analysis_id):
    # Generate a bar chart using Matplotlib
    try:
        labels = list(data.keys())
        values = list(data.values())

        plt.figure(figsize=(8, 4))
        plt.bar(labels, values)
        plt.xlabel('Leading Digit')
        plt.ylabel('Frequency')
        plt.title('Benford\'s Law Validation')
        
        graph_image_path = os.path.join('static', f'{analysis_id}-benfords_plot.png')
        plt.savefig(graph_image_path)

        return graph_image_path
    except Exception as e:
        print(e)
        return f'generate_bar_chart failed: {str(e)}'

