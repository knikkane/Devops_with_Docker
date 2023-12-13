import subprocess
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Git Log Parser API!"

# Gitlog route
@app.route('/gitlog', methods=['GET'])
def parse_git_log():    
        # Run git log command and save the output
        cmd_str = 'git log --pretty=format:"%an|%ad|%ae|%s"'
        git_log = subprocess.run([cmd_str], shell=True, stdout=subprocess.PIPE).stdout.decode('ISO-8859-1')

        # Split output into lines, parse lines and split into 4 components
        log_lines = git_log.strip().split('\n')
        data = []
        for line in log_lines:
                message, email, date, author = line.rsplit('|', 3)
                data.append({'Message': message.strip(), 'Email': email.strip(), 'Date': date.strip(), 'Author': author.strip()})

        # Create dataframe and rename colunms
        df = pd.DataFrame(data)
        df.columns = ['Author', 'Date', 'Email', 'Message']

        # Render the HTML page with the DataFrame
        return render_template('gitlog_table.html', git_log=df.to_dict(orient='records'))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
