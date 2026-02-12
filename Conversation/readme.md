# Airia API Testing Scripts

This directory contains two Python scripts for testing the Airia conversational AI API. These scripts demonstrate how to create conversations and execute pipeline operations.

## Scripts Overview

### 1. `get_conversation.py`
Creates a new conversation in the **development/staging** Airia environment.

### 2. `run_agent.py`
Executes a pipeline query against an existing conversation (e.g., "What was the latest F1 result?").

## Prerequisites

### Required Python Version
- Python 3.6 or higher

### Required Dependencies
Install the `requests` library:

```bash
pip install requests
```

Or on macOS with Homebrew:

```bash
brew install python-requests
```

## Configuration

Before running any script, you need to configure the following parameters:

### API Key
Replace the hardcoded API key in each script with your own Airia API key:

```python
api_key = "YOUR_API_KEY_HERE"
```

### User ID
Update the user ID if you want to use a different user:

```python
user_id = "YOUR_USER_ID_HERE"
```

### For `run_agent.py` Only
You also need to configure:

- **Pipeline Execution ID**: Update the UUID in the URL (line 9)
- **Conversation ID**: Update the `conversationId` in the payload (line 18)
- **User Input**: Modify the query/question (line 13)

## How to Test Each Script

### Testing `get_conversation.py` (Development)

This script creates a conversation in the development environment.

1. Open `get_conversation.py` and set your API key and user ID
2. Run the script:

```bash
python get_conversation.py
```

**Expected Output:**
- Status code (should be `200` or `201` for success)
- Response headers
- Raw response text
- Formatted JSON response with the new conversation details

**Example successful output:**
```
Status Code: 201
Response Headers:
  Content-Type: application/json
  ...

Response Text:
{"conversationId": "abc123...", "userId": "...", ...}

JSON Response:
{
  "conversationId": "abc123-...",
  "userId": "a820eeb8-ade0-4bcc-a16d-1e738ec8becb",
  "createdAt": "2024-01-15T10:30:00Z",
  ...
}
```

### Testing `run_agent.py` (Pipeline Execution)

This script sends a query to an AI pipeline and returns the response.

1. First, create a conversation using one of the scripts above and note the `conversationId`
2. Open `run_agent.py` and configure:
   - API key (line 23)
   - User ID (line 17)
   - Conversation ID (line 18)
   - Pipeline Execution ID in the URL (line 9)
   - Your question/query (line 13)

3. Run the script:

```bash
python run_agent.py
```

**Expected Output:**
The API response containing the AI's answer to your query, including any tool responses if `includeToolsResponse` is set to `True`.

**Example queries you can test:**
```python
"userInput": "What was the latest F1 result?"
"userInput": "Hi. My name is Reesy"
"userInput": "What is my name?"
```

## Configuration Options in `run_agent.py`

You can modify the payload to change behavior:

- `debug`: Set to `True` for debug information
- `asyncOutput`: Set to `True` for asynchronous responses
- `includeToolsResponse`: Set to `True` to see tool execution details

## Troubleshooting

### Common Issues

**Error: Module not found**
```
ModuleNotFoundError: No module named 'requests'
```
**Solution:** Install the requests library: `pip install requests`

**Error: 401 Unauthorized**
```
Status Code: 401
```
**Solution:** Check that your API key is valid and properly configured

**Error: 404 Not Found (run_agent.py)**
```
Status Code: 404
```
**Solution:** Verify that the Pipeline Execution ID in the URL exists and is correct

**Error: Invalid Conversation ID**
**Solution:** Make sure you've created a conversation first and are using the correct `conversationId`

## Security Considerations

**IMPORTANT:** These scripts currently contain hardcoded API keys, which is not secure for production use.

### Recommendations:
1. **Never commit API keys to version control**
2. Use environment variables instead:
   ```python
   import os
   api_key = os.environ.get('AIRIA_API_KEY')
   ```
3. Set the environment variable before running:
   ```bash
   export AIRIA_API_KEY="your-api-key-here"
   python get_conversation.py
   ```
4. Add `.env` files to `.gitignore` if using python-dotenv

## API Endpoints

- **Development:** `https://dev.api.airiadev.ai`

## Workflow Example

Here's a typical testing workflow:

1. **Create a conversation** (dev environment):
   ```bash
   python get_conversation.py
   ```
   Note the `conversationId` from the response.

2. **Execute a pipeline query**:
   Update `run_agent.py` with the `conversationId` and run:
   ```bash
   python run_agent.py
   ```

3. **Test follow-up questions** by changing the `userInput` and running again to test conversation context.

## Additional Notes

- All timestamps are in UTC and formatted as ISO 8601
- The `isBookmarked` field is set to `True` by default when creating conversations
- The scripts include comprehensive error handling and will print detailed error messages
