pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 --version || python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
