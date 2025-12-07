import { useEffect } from 'react'
import PropTypes from 'prop-types'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Clock, ChevronLeft, ChevronRight, History } from 'lucide-react'
import useReviewStore from '@/stores/reviewStore'
import { getReviews } from '@/lib/api'

export function ReviewHistory() {
    const { reviews, pagination, setReviews, setPagination, setError } = useReviewStore()

    useEffect(() => {
        loadReviews(1)
    }, [])

    const loadReviews = async (page) => {
        try {
            const response = await getReviews(page, pagination.limit)
            if (response.status === 'success') {
                setReviews(response.data.reviews)
                setPagination({
                    page: response.data.page,
                    limit: response.data.limit,
                    total: response.data.total,
                    totalPages: response.data.total_pages,
                })
            }
        } catch (error) {
            setError(error.message)
        }
    }

    const handlePageChange = (newPage) => {
        if (newPage >= 1 && newPage <= pagination.totalPages) {
            loadReviews(newPage)
        }
    }

    const getSentimentVariant = (sentiment) => {
        const variants = {
            positive: 'success',
            negative: 'destructive',
            neutral: 'warning',
        }
        return variants[sentiment?.toLowerCase()] || 'default'
    }

    const formatDate = (dateString) => {
        const date = new Date(dateString)
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
        })
    }

    return (
        <Card>
            <CardHeader>
                <CardTitle className="flex items-center gap-2">
                    <History className="h-5 w-5" />
                    Review History
                </CardTitle>
                <CardDescription>
                    {pagination.total > 0
                        ? `${pagination.total} review${pagination.total !== 1 ? 's' : ''} analyzed`
                        : 'No reviews yet'}
                </CardDescription>
            </CardHeader>
            <CardContent>
                {reviews.length > 0 ? (
                    <div className="space-y-4">
                        {/* Reviews List */}
                        <div className="space-y-3">
                            {reviews.map((review) => (
                                <div
                                    key={review.id}
                                    className="border rounded-lg p-4 hover:bg-accent/50 transition-colors"
                                >
                                    <div className="flex items-start justify-between gap-4 mb-2">
                                        <div className="flex-1 min-w-0">
                                            <p className="text-sm font-medium line-clamp-2 mb-1">
                                                {review.review_text}
                                            </p>
                                            <div className="flex items-center gap-2 text-xs text-muted-foreground">
                                                <Clock className="h-3 w-3" />
                                                {formatDate(review.created_at)}
                                            </div>
                                        </div>
                                        <div className="flex flex-col items-end gap-1">
                                            <Badge variant={getSentimentVariant(review.sentiment)}>
                                                {review.sentiment}
                                            </Badge>
                                            <span className="text-xs text-muted-foreground">
                                                {(review.confidence_score * 100).toFixed(0)}%
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>

                        {/* Pagination */}
                        {pagination.totalPages > 1 && (
                            <div className="flex items-center justify-between pt-4 border-t">
                                <p className="text-sm text-muted-foreground">
                                    Page {pagination.page} of {pagination.totalPages}
                                </p>
                                <div className="flex gap-2">
                                    <Button
                                        variant="outline"
                                        size="sm"
                                        onClick={() => handlePageChange(pagination.page - 1)}
                                        disabled={pagination.page === 1}
                                    >
                                        <ChevronLeft className="h-4 w-4" />
                                        Previous
                                    </Button>
                                    <Button
                                        variant="outline"
                                        size="sm"
                                        onClick={() => handlePageChange(pagination.page + 1)}
                                        disabled={pagination.page === pagination.totalPages}
                                    >
                                        Next
                                        <ChevronRight className="h-4 w-4" />
                                    </Button>
                                </div>
                            </div>
                        )}
                    </div>
                ) : (
                    <div className="text-center py-8">
                        <History className="h-12 w-12 mx-auto text-muted-foreground/50 mb-3" />
                        <p className="text-sm text-muted-foreground">
                            No reviews yet. Submit your first review above!
                        </p>
                    </div>
                )}
            </CardContent>
        </Card>
    )
}

ReviewHistory.propTypes = {}
