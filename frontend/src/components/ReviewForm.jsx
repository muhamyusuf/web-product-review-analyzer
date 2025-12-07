import { useState } from 'react'
import PropTypes from 'prop-types'
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { Loader2, Send } from 'lucide-react'

export function ReviewForm({ onSubmit, isLoading, error }) {
    const [reviewText, setReviewText] = useState('')

    const handleSubmit = (e) => {
        e.preventDefault()
        if (reviewText.trim()) {
            onSubmit(reviewText)
        }
    }

    const handleClear = () => {
        setReviewText('')
    }

    return (
        <Card className="w-full">
            <CardHeader>
                <CardTitle>Submit Product Review</CardTitle>
                <CardDescription>
                    Enter your product review below. Our AI will analyze the sentiment and extract key points.
                </CardDescription>
            </CardHeader>
            <CardContent>
                <form onSubmit={handleSubmit} className="space-y-4">
                    <div className="space-y-2">
                        <Textarea
                            placeholder="Write your product review here... (supports multiple languages)"
                            value={reviewText}
                            onChange={(e) => setReviewText(e.target.value)}
                            rows={6}
                            disabled={isLoading}
                            className="resize-none"
                        />
                        <p className="text-xs text-muted-foreground">
                            Minimum 10 characters • {reviewText.length} characters
                        </p>
                    </div>

                    {error && (
                        <Alert variant="destructive" className="animate-in">
                            <AlertDescription>{error}</AlertDescription>
                        </Alert>
                    )}

                    <div className="flex gap-2">
                        <Button
                            type="submit"
                            disabled={isLoading || reviewText.trim().length < 10}
                            className="flex-1"
                        >
                            {isLoading ? (
                                <>
                                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                                    Analyzing...
                                </>
                            ) : (
                                <>
                                    <Send className="mr-2 h-4 w-4" />
                                    Analyze Review
                                </>
                            )}
                        </Button>
                        <Button
                            type="button"
                            variant="outline"
                            onClick={handleClear}
                            disabled={isLoading || !reviewText}
                        >
                            Clear
                        </Button>
                    </div>
                </form>
            </CardContent>
        </Card>
    )
}

ReviewForm.propTypes = {
    onSubmit: PropTypes.func.isRequired,
    isLoading: PropTypes.bool,
    error: PropTypes.string,
}
