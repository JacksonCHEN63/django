pipelineJob('pipelinejob3_jenkinsfile_casc') {
  definition {
    cpsScm {
      scm {
        git {
          remote {
            url('https://github.com/JacksonCHEN63/Django.git')
          }
          branch('*/master')
        }
      }
      lightweight()
    }
  }
}
