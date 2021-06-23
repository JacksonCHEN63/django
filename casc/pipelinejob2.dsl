pipelineJob('pipelinejob2') {
    definition {
        cps {
            script('''
node ("jackson") {
    stage("checkout") {
        echo "hiiiiiiiii"
    } 
}            
            ''')
            sandbox()
        }
    }
}
