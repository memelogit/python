pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'yum install python3'
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
