from fastapi import APIRouter, File, UploadFile, Form, Query
from app.services.the_virus_total import scanning_with_virustotal
from app.services.Ai_mistral import result_summarizing
from app.services.summary_scan import virustotal_summarization

routing = APIRouter(prefix = "/scan", tags = ["Scanner"])

@routing.post("/upload-file")
async def scanning_file(file: UploadFile = File(...)):
    context = await file.read()
    result_virustotal = scanning_with_virustotal(file_bytes = context, filename = file.filename)
    virutt_summary = virustotal_summarization(result_virustotal)
    

    ai_agent_response = result_summarizing("Can you confirm if this file is safe? Explain.", virutt_summary)
    return {
        "1- Virus Total": result_virustotal,
        "2- AI_result": ai_agent_response
    }

@routing.get("/scan-url")
async def scanning_url(url: str = Query(..., description = "Please paste the the file url or resource to scan")):
    result_virustotal = scanning_with_virustotal(url = url)
    virutt_summary = virustotal_summarization(result_virustotal)
    ai_agent_response = result_summarizing("Can you confirm if this file is safe? Explain.", virutt_summary)
    return {
        "1- Virus Total": result_virustotal,
        "2- AI_result": ai_agent_response
    }
