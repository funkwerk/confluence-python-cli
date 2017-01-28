task default: :audit

desc 'Publishes the PyPi'
task push: :generate
task :push do
  sh 'python3 setup.py sdist upload'
end

desc 'Checks style'
task audit: :rubocop
task :audit do
  ignores = %w(
    B901
    C812
    D100 D101 D102 D103
    E121 E201 E225 E231 E302 E303 E305 E401 E501 I201
    F811 F841
    I101
    N802 N803
    P101
    Q000
  )

  FILES = FileList[%w(*.py)]
  sh "flake8 --ignore='#{ignores * ','}' #{FILES}"
  sh "pylint -E #{FILES}"
end

desc 'Checks ruby style'
task :rubocop do
  sh 'rubocop'
end

task :generate do
  sh 'pandoc --from=markdown --to=rst --output=README.rst README.md'
end
