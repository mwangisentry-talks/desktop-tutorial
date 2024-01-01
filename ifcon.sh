#!/bin/bash

ifconfig -a
ip addr show | grep inet6

arp -a
