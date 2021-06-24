pipelineJob('demo/pipelinejob1_casc') {
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
