pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Compile') {
			steps {
				sh 'python add2nums.py'
			}
		}
		stage('Test') {
			steps {
				sh 'python test.py'
			}
		}
    }
}
