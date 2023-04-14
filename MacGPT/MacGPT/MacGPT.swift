//
//  MacGPT.swift
//  MacGPT
//
//  Created by Daniel Santiago on 4/14/23.
//
import Foundation

struct ChatGPT {
    private let apiKey = "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"
    
    func sendMessage(message: String, completion: @escaping (Result<String, Error>) -> Void) {
        guard let url = URL(string: "https://api.openai.com/v1/engines/davinci-codex/completions") else {
            completion(.failure(NSError(domain: "", code: -1, userInfo: [NSLocalizedDescriptionKey: "Invalid URL"])))
            return
        }
        
        let prompt = "You: \(message)\nGPT-3:"
        let requestBody: [String: Any] = [
            "prompt": prompt,
            "max_tokens": 50
        ]
        
        do {
            let data = try JSONSerialization.data(withJSONObject: requestBody, options: [])
            var request = URLRequest(url: url)
            request.httpMethod = "POST"
            request.httpBody = data
            request.addValue("Bearer \(apiKey)", forHTTPHeaderField: "Authorization")
            request.addValue("application/json", forHTTPHeaderField: "Content-Type")
            
            let task = URLSession.shared.dataTask(with: request) { data, response, error in
                if let error = error {
                    completion(.failure(error))
                    return
                }
                
                guard let data = data else {
                    completion(.failure(NSError(domain: "", code: -1, userInfo: [NSLocalizedDescriptionKey: "No data received"])))
                    return
                }
                
                do {
                    if let json = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any],
                       let choices = json["choices"] as? [[String: Any]],
                       let firstChoice = choices.first,
                       let text = firstChoice["text"] as? String {
                        completion(.success(text))
                    } else {
                        completion(.failure(NSError(domain: "", code: -1, userInfo: [NSLocalizedDescriptionKey: "Invalid JSON format"])))
                    }
                } catch {
                    completion(.failure(error))
                }
            }
            task.resume()
        } catch {
            completion(.failure(error))
        }
    }
}
