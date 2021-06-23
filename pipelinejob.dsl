pipelineJob('Configuration as Code Plugin') {
    definition {
        cps {
            script('''
node ("jackson") {
    stage("checkout") {
        echo "hello"
    } 
}            
            ''')
            sandbox()
        }
    }
}
