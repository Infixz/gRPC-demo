#!/bin/bash

# Runs the protoc with gRPC plugin to generate protocol messages and gRPC stubs.
# protoc --proto_path=/home/linuxdev-12/homer/gRPC/protos --python_out=/home/linuxdev-12/homer/gRPC/demo1 /home/linuxdev-12/homer/gRPC/protos/qrlink.proto
protoc -I /home/linuxdev-12/homer/gRPC/protos --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` /home/linuxdev-12/homer/gRPC/protos/qrlink.proto
