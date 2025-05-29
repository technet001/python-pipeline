pipeline {
    agent  any
    
    stages {
        stage('Build') {
            steps {
                sh 'sudo python --version'
            }
        }
        stage('Compile') {
			steps {
				sh 'sudo python add2nums.py'
			}
		}
		stage('Test') {
			steps {
				sh 'sudo python test.py'
			}
		}
    }
}
