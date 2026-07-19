pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Jenkins is alive'
                sh 'docker --version'
                sh 'whoami'
            }
        }
    }
}
