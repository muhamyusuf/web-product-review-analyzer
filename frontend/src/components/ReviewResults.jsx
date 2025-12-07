import PropTypes from 'prop-types'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { CheckCircle2, XCircle, MinusCircle, TrendingUp, Sparkles } from 'lucide-react'

export function ReviewResults({ analysis }) {
    if (!analysis) return null

    const { data } = analysis
    const { sentiment, confidence_score, key_points, review_text } = data

    // Parse key points JSON
    let keyPointsArray = []
    try {
        keyPointsArray = JSON.parse(key_points)
    } catch (e) {
        keyPointsArray = [key_points]
    }

    // Sentiment configuration
    const sentimentConfig = {
        positive: {
            icon: CheckCircle2,
            variant: 'success',
            color: 'text-green-600 dark:text-green-400',
            bgColor: 'bg-green-50 dark:bg-green-950',
            label: 'Positive',
        },
        negative: {
            icon: XCircle,
            variant: 'destructive',
            color: 'text-red-600 dark:text-red-400',
            bgColor: 'bg-red-50 dark:bg-red-950',
            label: 'Negative',
        },
        neutral: {
            icon: MinusCircle,
            variant: 'warning',
            color: 'text-yellow-600 dark:text-yellow-400',
            bgColor: 'bg-yellow-50 dark:bg-yellow-950',
            label: 'Neutral',
        },
    }

    const config = sentimentConfig[sentiment.toLowerCase()] || sentimentConfig.neutral
    const SentimentIcon = config.icon

    return (
        <div className="space-y-4 animate-in">
            {/* Sentiment Analysis Card */}
            <Card className={config.bgColor}>
                <CardHeader>
                    <div className="flex items-center justify-between">
                        <CardTitle className="flex items-center gap-2">
                            <TrendingUp className="h-5 w-5" />
                            Sentiment Analysis
                        </CardTitle>
                        <Badge variant={config.variant} className="text-sm">
                            <SentimentIcon className="mr-1 h-4 w-4" />
                            {config.label}
                        </Badge>
                    </div>
                    <CardDescription>AI-powered sentiment detection</CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                    {/* Confidence Score */}
                    <div className="space-y-2">
                        <div className="flex justify-between text-sm">
                            <span className="font-medium">Confidence Score</span>
                            <span className={config.color}>
                                {(confidence_score * 100).toFixed(1)}%
                            </span>
                        </div>
                        <div className="w-full bg-secondary rounded-full h-2.5">
                            <div
                                className={`h-2.5 rounded-full transition-all duration-300 ${sentiment === 'positive'
                                        ? 'bg-green-600'
                                        : sentiment === 'negative'
                                            ? 'bg-red-600'
                                            : 'bg-yellow-600'
                                    }`}
                                style={{ width: `${confidence_score * 100}%` }}
                            />
                        </div>
                    </div>

                    {/* Review Text */}
                    <div className="space-y-2">
                        <p className="text-sm font-medium">Review Text:</p>
                        <p className="text-sm text-muted-foreground italic border-l-4 pl-4 py-2">
                            "{review_text}"
                        </p>
                    </div>
                </CardContent>
            </Card>

            {/* Key Points Card */}
            <Card>
                <CardHeader>
                    <CardTitle className="flex items-center gap-2">
                        <Sparkles className="h-5 w-5" />
                        Key Points
                    </CardTitle>
                    <CardDescription>AI-extracted insights from the review</CardDescription>
                </CardHeader>
                <CardContent>
                    {keyPointsArray.length > 0 ? (
                        <ul className="space-y-3">
                            {keyPointsArray.map((point, index) => (
                                <li key={index} className="flex gap-3 items-start">
                                    <span className="flex-shrink-0 w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-semibold mt-0.5">
                                        {index + 1}
                                    </span>
                                    <span className="text-sm leading-relaxed">{point}</span>
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <p className="text-sm text-muted-foreground">No key points extracted.</p>
                    )}
                </CardContent>
            </Card>
        </div>
    )
}

ReviewResults.propTypes = {
    analysis: PropTypes.shape({
        data: PropTypes.shape({
            id: PropTypes.number,
            review_text: PropTypes.string,
            sentiment: PropTypes.string,
            confidence_score: PropTypes.number,
            key_points: PropTypes.string,
            created_at: PropTypes.string,
        }),
    }),
}
