pipeline {
    agent any
    
    stages {
        stage('Python Check') {
            steps {
                sh 'python3 --version'
                sh 'python3 -c "import sys; print(sys.path)"'
            }
        }
        
        stage('Run My Scripts') {
            steps {
                sh 'python3 your_current_script.py'
            }
        }
        
        stage('Lint Check') {
            steps {
                sh 'pip3 install flake8 || true'
                sh 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics || true'
            }
        }
    }
}