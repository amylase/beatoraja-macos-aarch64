# beatoraja on macOS with Apple Silicon

Tiny wrapper of [beatoraja](https://github.com/exch-bms2/beatoraja) for macOS running on Apple Silicon.

## Prerequisites

* Rosetta 2 is installed

## Usage

run beatoraja.command

## How it works

Runs beatoraja with [Liberica JDK 17 x86_64](https://bell-sw.com/pages/downloads/#jdk-17-lts). This wrapper implicitly uses Rosetta 2. For this reason, this code may work on Intel Mac as well (NOT tested!).
