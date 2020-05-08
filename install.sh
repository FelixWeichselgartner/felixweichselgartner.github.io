sudo dnf install ruby ruby-devel
gem install commonmarker -v '0.17.13' --source 'https://rubygems.org/'
sudo gem pristine eventmachine --version 1.2.7
sudo gem pristine http_parser.rb --version 0.6.0
sudo gem pristine nokogiri --version 1.10.9
sudo gem pristine ffi --version 1.12.2
bundle install

