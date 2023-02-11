#!/usr/bin/env ruby

require 'getoptlong'

HELPMESSAGE = "
p
instrukcja do p
"

opts = GetoptLong.new(
  ['--help','-h',GetoptLong::NO_ARGUMENT],
  ['--inverse','-v',GetoptLong::NO_ARGUMENT],
  ['--file','-f',GetoptLong::REQUIRED_ARGUMENT]
)

opts.each do |arg,val|
  case arg
  when '--inverse'    then INVERSE = true
  when '--file'       then ARGV << val
  when '--help'       then puts HELPMESSAGE; exit 0
  end
end

INVERSE = false unless defined? INVERSE

abort "Wyr reg not given" if ARGV.empty?

re = /#{ARGV.shift}/

while l = gets
  puts l if (INVERSE ? (l !~ re) :  (l =~ re) )
end
