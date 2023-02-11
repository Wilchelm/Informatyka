#!/usr/bin/env ruby
# coding: utf-8
a=ARGV.shift
#puts readlines.map{|l| l.scan a.shift}.flatten.map(&:to_i).reduce(0,:+)

while l=gets
	if l.match?(a) == true
		puts l
	end
end
