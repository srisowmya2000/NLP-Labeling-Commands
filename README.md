**Overview**
This repository contains a security tool that uses Natural Language Processing (NLP) to analyze shell commands and classify them as benign, suspicious, or malicious. By leveraging NLP transformations, the tool can identify potentially harmful commands before they are executed, helping to protect systems from malicious activity.

Note: This is an early version that may be glitchy - I'm working on releasing a better version soon. 

**Features**

Analyzes shell and system commands for security threats
Uses NLP transformations to understand command semantics
Classifies commands into three categories:
_
Benign: Safe commands that pose no security threat
Suspicious: Commands that may have legitimate uses but could potentially be harmful
Malicious: Commands that are highly likely to cause harm or compromise system security_


Provides HTML output for easy visualization of results

**How It Works**
The tool employs several NLP techniques to analyze and classify shell commands:

Tokenization: Breaks down commands into individual components
Feature Extraction: Identifies key characteristics of commands that may indicate malicious intent
Semantic Analysis: Understands the purpose and potential impact of commands
Pattern Recognition: Compares commands against known malicious patterns
Classification: Uses a trained model to categorise commands based on their potential risk


