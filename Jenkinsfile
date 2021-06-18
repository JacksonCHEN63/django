pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                sh 'df -h'
            }
        }

        stage('Stage 2') {
	  when {
            branch "dev"
	  }
            steps {
                echo 'hello'
            }
        }
    }
}
