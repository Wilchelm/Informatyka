#!/usr/bin/env ruby
# coding: utf-8
h = Hash.new

gets.each_line { |line|
  words = line.split
  words.each { |w|
    if h.has_key?(w)
      h[w] = h[w] + 1
    else
      h[w] = 1
    end
  }
}

# sort the hash by value, and then print it in this sorted order
h.sort{|a,b| a[1]<=>b[1]}.each { |elem|
  puts "#{elem[0]} #{elem[1]}"
}
