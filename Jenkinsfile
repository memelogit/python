pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 hello.py'
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
