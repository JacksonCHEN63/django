pipelineJob('Configuration as Code Plugin') {
    definition {
        cps {
            script('''
agent any {
    stage("checkout") {
        echo "hello"
    } 
}            
            ''')
            sandbox()
        }
    }
}
