pipeline{
    agent any
    stages{
        stage ("clone ERMS project code from github"){
            steps{
                echo "cloning from github repo"
                git url:"https://github.com/Sahulinkan7/ERMS.git",branch:"main"
            }
            post{
                success{
                    echo "github clone done"
                }
                failure{
                    echo "cloning failed"
                }
                
            }
        }
        
    }
}