#!/usr/bin/env ruby
# coding: utf-8

#while l=gets
#	if l.match?(/#.*/) == false
#		puts l
#	end
#end
defy = {}

while l=gets
	if l =~ /^\s*#define\s*(\S+)\s*(.*)$/
		defy[$1] = $2
		next
	end

	defy.each{|k,v| l.gsub! k, v }
	puts l
end

