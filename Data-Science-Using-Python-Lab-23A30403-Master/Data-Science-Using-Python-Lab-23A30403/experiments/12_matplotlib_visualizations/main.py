"""
Experiment 12: Matplotlib Visualizations
Course Code: 23A30403 - Data Science Using Python Lab
"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Experiment 12: Matplotlib Visualizations ===")
    print("Generating interactive visualization window...")
    
    # Data definition
    categories = ['Python', 'Java', 'C++', 'R', 'SQL']
    popularity = [85, 70, 60, 50, 75]
    np.random.seed(42)
    scores = np.random.normal(70, 10, 200)
    x_line = np.linspace(0, 10, 100)
    y_line = np.sin(x_line)
    scatter_x = np.random.rand(50)
    scatter_y = np.random.rand(50)
    
    fig = plt.figure(figsize=(14, 10))
    fig.suptitle('Data Science Lab Visualizations Suite', fontsize=16, fontweight='bold')
    
    # a. Bar Graph
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.bar(categories, popularity, color='skyblue')
    ax1.set_title('a. Bar Graph (Popularity)')
    ax1.set_ylabel('Score')
    
    # b. Pie Chart
    ax2 = fig.add_subplot(2, 3, 2)
    ax2.pie(popularity, labels=categories, autopct='%1.1f%%', startangle=140)
    ax2.set_title('b. Pie Chart (Distribution)')
    
    # c. Box Plot
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.boxplot(scores, patch_artist=True)
    ax3.set_title('c. Box Plot (Scores)')
    
    # d. Histogram
    ax4 = fig.add_subplot(2, 3, 4)
    ax4.hist(scores, bins=15, color='lightgreen', edgecolor='black')
    ax4.set_title('d. Histogram (Frequency)')
    
    # e. Line Chart
    ax5 = fig.add_subplot(2, 3, 5)
    ax5.plot(x_line, y_line, color='red', label='Sine Wave')
    ax5.set_title('e. Line Chart')
    ax5.legend()
    
    # f. Scatter Plot
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.scatter(scatter_x, scatter_y, color='purple', alpha=0.7)
    ax6.set_title('f. Scatter Plot')
    
    plt.tight_layout()
    print("Displaying plots. Close the figure window to continue...")
    plt.show()

if __name__ == "__main__":
    main()
