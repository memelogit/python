pipeline {
    agent {
        docker {
            image 'python:3.8' // O la versión que necesites
            args '-u' // Opcional: ejecuta como usuario no root
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'python --version'
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
