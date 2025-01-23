from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
import re

matplotlib.use('Agg')  # Use Matplotlib only for saving images

app = Flask(__name__)

def create_pie_chart(university_name, positive_percentage, negative_percentage):
    pie_chart_dir = 'universite_analizi/static/pie_charts'
    safe_university_name = re.sub(r'\s+', '_', university_name)  # Replace spaces with underscores
    
    labels = ['Positive', 'Negative']
    sizes = [positive_percentage, negative_percentage]
    colors = ['#66c2a5', '#fc8d62']
    plt.figure(figsize=(6, 6))
    plt.gcf().patch.set_facecolor('#f0f0f5') 
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio for better visualization
    
    file_path = os.path.join(pie_chart_dir, f'{safe_university_name}.png')
    plt.savefig(file_path)  # Save the chart
    plt.close()  # Close the chart
    print(f"Chart saved: {file_path}")

@app.route('/result', methods=['POST'])
def result():
    university = request.form['university'].strip().title()
    filtered_data = pd.read_csv('filtrelenmis_yuzdeler.csv')
    filtered_data.iloc[:, 5] = filtered_data.iloc[:, 5].str.strip().str.title()

    university_row = filtered_data[filtered_data.iloc[:, 5] == university]

    if university_row.empty:
        return "University not found."

    positive_percentage = university_row['Pozitif Yüzde'].values[0]
    negative_percentage = university_row['Negatif Yüzde'].values[0]
    create_pie_chart(university, positive_percentage, negative_percentage)

    safe_university_name = re.sub(r'\s+', '_', university)
    pie_chart_url = f"static/pie_charts/{safe_university_name}.png"

    return render_template('result.html', university_name=university, pie_chart_url=pie_chart_url)

@app.route('/top_10_universities')
def top_10_universities():
    image_url = "static/images/en_yuksek_10_pozitif_yuzde_universiteler.png"
    return render_template('top_10_universities.html', image_url=image_url)

@app.route('/')
def index():
    df = pd.read_csv('filtrelenmis_yuzdeler.csv')
    university_names = df.iloc[:, 5].unique()
    return render_template('index.html', university_names=university_names)

if __name__ == '__main__':
    app.run(debug=True)
