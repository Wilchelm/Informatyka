#!/usr/bin/env ruby
# coding: utf-8

#puts readlines.map{|l| l.scan /\d+/}.flatten.map(&:to_i).reduce(0){|a,b| a+b}
puts readlines.map{|l| l.scan /\d+/}.flatten.map(&:to_i).reduce(0,:+)
