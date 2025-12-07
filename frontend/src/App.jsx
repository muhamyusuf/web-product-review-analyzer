import { useState } from 'react'
import { ThemeToggle } from './components/ThemeToggle'
import { ReviewForm } from './components/ReviewForm'
import { ReviewResults } from './components/ReviewResults'
import { ReviewHistory } from './components/ReviewHistory'
import { Brain, Sparkles } from 'lucide-react'
import useReviewStore from './stores/reviewStore'
import { analyzeReview } from './lib/api'
import './index.css'

function App() {
    const {
        currentAnalysis,
        isLoading,
        error,
        setCurrentAnalysis,
        setLoading,
        setError,
        clearError,
        addReview,
    } = useReviewStore()

    const [showHistory, setShowHistory] = useState(false)

    const handleSubmitReview = async (reviewText) => {
        clearError()
        setLoading(true)

        try {
            const result = await analyzeReview(reviewText)
            setCurrentAnalysis(result)

            // Add to history
            if (result.status === 'success' && result.data) {
                addReview(result.data)
            }

            // Show history after successful analysis
            setShowHistory(true)
        } catch (err) {
            setError(err.message)
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="min-h-screen bg-background">
            {/* Header */}
            <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
                <div className="container mx-auto px-4 py-4">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-3">
                            <div className="bg-primary text-primary-foreground rounded-lg p-2">
                                <Brain className="h-6 w-6" />
                            </div>
                            <div>
                                <h1 className="text-2xl font-bold flex items-center gap-2">
                                    Product Review Analyzer
                                    <Sparkles className="h-5 w-5 text-yellow-500" />
                                </h1>
                                <p className="text-sm text-muted-foreground">
                                    AI-powered sentiment analysis & key insights
                                </p>
                            </div>
                        </div>
                        <ThemeToggle />
                    </div>
                </div>
            </header>

            {/* Main Content */}
            <main className="container mx-auto px-4 py-8">
                <div className="max-w-5xl mx-auto space-y-8">
                    {/* Review Form */}
                    <ReviewForm
                        onSubmit={handleSubmitReview}
                        isLoading={isLoading}
                        error={error}
                    />

                    {/* Results */}
                    {currentAnalysis && <ReviewResults analysis={currentAnalysis} />}

                    {/* History */}
                    {/* {showHistory && <ReviewHistory />} */}
                    <ReviewHistory />
                </div>
            </main>

            {/* Footer */}
            <footer className="border-t mt-16">
                <div className="container mx-auto px-4 py-6">
                    <div className="text-center text-sm text-muted-foreground">
                        <p>
                            Powered by{' '}
                            <span className="font-semibold text-foreground">Hugging Face</span> &{' '}
                            <span className="font-semibold text-foreground">Google Gemini AI</span>
                        </p>
                        <p className="mt-1">
                            Built with React, Vite, Pyramid & PostgreSQL
                        </p>
                        <p>
                            Build with 💖 by Muhammad Yusuf NIM 122140193 😁
                        </p>
                    </div>
                </div>
            </footer>
        </div>
    )
}

export default App
