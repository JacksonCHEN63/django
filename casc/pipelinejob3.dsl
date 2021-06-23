pipelineJob('job-dsl-plugin') {
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
